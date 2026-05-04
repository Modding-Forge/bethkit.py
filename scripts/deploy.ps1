# Deploy script — builds bethkit_ffi.dll (release) and assembles a ready-to-use
# bethkit package folder under deploy/bethkit/.
#
# Usage: pwsh scripts/deploy.ps1
#        pwsh scripts/deploy.ps1 -OutDir my_project/bethkit

param(
    [string]$OutDir = "deploy\bethkit"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$RepoRoot   = Split-Path -Parent $PSScriptRoot
$RustRoot   = Join-Path (Split-Path -Parent $RepoRoot) "bethkit"
$SrcDir     = Join-Path $RepoRoot "src\bethkit"
$DllSrc     = Join-Path $RustRoot "target\release\bethkit_ffi.dll"
$OutDirFull = Join-Path $RepoRoot $OutDir

Write-Host "==> Building bethkit_ffi (release)..."
Push-Location $RustRoot
try {
    cargo build --release -p bethkit-ffi
    if ($LASTEXITCODE -ne 0) { throw "cargo build failed" }
} finally {
    Pop-Location
}

Write-Host "==> Assembling deploy folder: $OutDirFull"
if (Test-Path $OutDirFull) {
    Remove-Item -Recurse -Force $OutDirFull
}
New-Item -ItemType Directory -Force $OutDirFull | Out-Null

# Copy all Python package files.
Get-ChildItem -Path $SrcDir -File | Copy-Item -Destination $OutDirFull

# Copy the DLL next to the Python files so _ffi.py can find it automatically.
if (-not (Test-Path $DllSrc)) {
    throw "DLL not found at: $DllSrc"
}
Copy-Item $DllSrc $OutDirFull

Write-Host "==> Done."
Write-Host "    $OutDirFull"
Get-ChildItem $OutDirFull | Format-Table Name, Length -AutoSize
