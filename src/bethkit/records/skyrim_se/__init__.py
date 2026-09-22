"""
Copyright (c) Modding Forge

Lazily loaded Skyrim SE record models generated from xEdit.
"""

from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .aact import ActionRecord as ActionRecord
    from .achr import PlacedNpcRecord as PlacedNpcRecord
    from .acti import ActivatorRecord as ActivatorRecord
    from .addn import AddonNodeRecord as AddonNodeRecord
    from .alch import IngestibleRecord as IngestibleRecord
    from .ammo import AmmunitionRecord as AmmunitionRecord
    from .anio import AnimatedObjectRecord as AnimatedObjectRecord
    from .appa import AlchemicalApparatusRecord as AlchemicalApparatusRecord
    from .arma import ArmorAddonRecord as ArmorAddonRecord
    from .armo import ArmorRecord as ArmorRecord
    from .arto import ArtObjectRecord as ArtObjectRecord
    from .aspc import AcousticSpaceRecord as AcousticSpaceRecord
    from .astp import AssociationTypeRecord as AssociationTypeRecord
    from .avif import ActorValueInformationRecord as ActorValueInformationRecord
    from .book import BookRecord as BookRecord
    from .bptd import BodyPartDataRecord as BodyPartDataRecord
    from .cams import CameraShotRecord as CameraShotRecord
    from .cell import CellRecord as CellRecord
    from .clas import ClassValueRecord as ClassValueRecord
    from .cldc import CldcRecord as CldcRecord
    from .clfm import ColorRecord as ColorRecord
    from .clmt import ClimateRecord as ClimateRecord
    from .cobj import ConstructibleObjectRecord as ConstructibleObjectRecord
    from .coll import CollisionLayerRecord as CollisionLayerRecord
    from .cont import ContainerRecord as ContainerRecord
    from .cpth import CameraPathRecord as CameraPathRecord
    from .csty import CombatStyleRecord as CombatStyleRecord
    from .debr import DebrisRecord as DebrisRecord
    from .dial import DialogTopicRecord as DialogTopicRecord
    from .dlbr import DialogBranchRecord as DialogBranchRecord
    from .dlvw import DialogViewRecord as DialogViewRecord
    from .dobj import DefaultObjectManagerRecord as DefaultObjectManagerRecord
    from .door import DoorRecord as DoorRecord
    from .dual import DualCastDataRecord as DualCastDataRecord
    from .eczn import EncounterZoneRecord as EncounterZoneRecord
    from .efsh import EffectShaderRecord as EffectShaderRecord
    from .ench import ObjectEffectRecord as ObjectEffectRecord
    from .equp import EquipTypeRecord as EquipTypeRecord
    from .expl import ExplosionRecord as ExplosionRecord
    from .eyes import EyesRecord as EyesRecord
    from .fact import FactionRecord as FactionRecord
    from .flor import FloraRecord as FloraRecord
    from .flst import FormIdListRecord as FormIdListRecord
    from .fstp import FootstepRecord as FootstepRecord
    from .fsts import FootstepSetRecord as FootstepSetRecord
    from .furn import FurnitureRecord as FurnitureRecord
    from .glob import GlobalValueRecord as GlobalValueRecord
    from .gmst import GameSettingRecord as GameSettingRecord
    from .gras import GrassRecord as GrassRecord
    from .hair import HairRecord as HairRecord
    from .hazd import HazardRecord as HazardRecord
    from .hdpt import HeadPartRecord as HeadPartRecord
    from .idle import IdleAnimationRecord as IdleAnimationRecord
    from .idlm import IdleMarkerRecord as IdleMarkerRecord
    from .imad import ImageSpaceAdapterRecord as ImageSpaceAdapterRecord
    from .imgs import ImageSpaceRecord as ImageSpaceRecord
    from .info import InfoRecord as InfoRecord
    from .ingr import IngredientRecord as IngredientRecord
    from .ipct import ImpactRecord as ImpactRecord
    from .ipds import ImpactDataSetRecord as ImpactDataSetRecord
    from .keym import KeyRecord as KeyRecord
    from .kywd import KeywordRecord as KeywordRecord
    from .land import LandscapeRecord as LandscapeRecord
    from .lcrt import LocationReferenceTypeRecord as LocationReferenceTypeRecord
    from .lctn import LocationRecord as LocationRecord
    from .lens import LensFlareRecord as LensFlareRecord
    from .lgtm import LightingTemplateRecord as LightingTemplateRecord
    from .ligh import LightRecord as LightRecord
    from .lscr import LoadScreenRecord as LoadScreenRecord
    from .ltex import LandscapeTextureRecord as LandscapeTextureRecord
    from .lvli import LeveledItemRecord as LeveledItemRecord
    from .lvln import LeveledNpcRecord as LeveledNpcRecord
    from .lvsp import LeveledSpellRecord as LeveledSpellRecord
    from .mato import MaterialObjectRecord as MaterialObjectRecord
    from .matt import MaterialTypeRecord as MaterialTypeRecord
    from .mesg import MessageRecord as MessageRecord
    from .mgef import MagicEffectRecord as MagicEffectRecord
    from .misc import MiscItemRecord as MiscItemRecord
    from .movt import MovementTypeRecord as MovementTypeRecord
    from .mstt import MoveableStaticRecord as MoveableStaticRecord
    from .musc import MusicTypeRecord as MusicTypeRecord
    from .must import MusicTrackRecord as MusicTrackRecord
    from .navi import NavmeshInfoMapRecord as NavmeshInfoMapRecord
    from .navm import NavmeshRecord as NavmeshRecord
    from .npc import NpcRecord as NpcRecord
    from .otft import OutfitRecord as OutfitRecord
    from .pack import PackageRecord as PackageRecord
    from .parw import PlacedArrowRecord as PlacedArrowRecord
    from .pbar import PlacedBarrierRecord as PlacedBarrierRecord
    from .pbea import PlacedBeamRecord as PlacedBeamRecord
    from .pcon import PlacedConeVoiceRecord as PlacedConeVoiceRecord
    from .perk import PerkRecord as PerkRecord
    from .pfla import PlacedFlameRecord as PlacedFlameRecord
    from .pgre import PlacedProjectileRecord as PlacedProjectileRecord
    from .phzd import PlacedHazardRecord as PlacedHazardRecord
    from .plyr import PlayerReferenceRecord as PlayerReferenceRecord
    from .pmis import PlacedMissileRecord as PlacedMissileRecord
    from .proj import ProjectileRecord as ProjectileRecord
    from .pwat import PwatRecord as PwatRecord
    from .qust import QuestRecord as QuestRecord
    from .race import RaceRecord as RaceRecord
    from .refr import PlacedObjectRecord as PlacedObjectRecord
    from .regn import RegionRecord as RegionRecord
    from .rela import RelationshipRecord as RelationshipRecord
    from .revb import ReverbParametersRecord as ReverbParametersRecord
    from .rfct import VisualEffectRecord as VisualEffectRecord
    from .rgdl import RgdlRecord as RgdlRecord
    from .scen import SceneRecord as SceneRecord
    from .scol import StaticCollectionRecord as StaticCollectionRecord
    from .scpt import ScptRecord as ScptRecord
    from .scrl import ScrollRecord as ScrollRecord
    from .shou import ShoutRecord as ShoutRecord
    from .slgm import SoulGemRecord as SoulGemRecord
    from .smbn import (
        StoryManagerBranchNodeRecord as StoryManagerBranchNodeRecord,
    )
    from .smen import StoryManagerEventNodeRecord as StoryManagerEventNodeRecord
    from .smqn import StoryManagerQuestNodeRecord as StoryManagerQuestNodeRecord
    from .snct import SoundCategoryRecord as SoundCategoryRecord
    from .sndr import SoundDescriptorRecord as SoundDescriptorRecord
    from .sopm import SoundOutputModelRecord as SoundOutputModelRecord
    from .soun import SoundMarkerRecord as SoundMarkerRecord
    from .spel import SpellRecord as SpellRecord
    from .spgd import (
        ShaderParticleGeometryRecord as ShaderParticleGeometryRecord,
    )
    from .stat import StaticRecord as StaticRecord
    from .tact import TalkingActivatorRecord as TalkingActivatorRecord
    from .tes4 import MainFileHeaderRecord as MainFileHeaderRecord
    from .tree import TreeRecord as TreeRecord
    from .txst import TextureSetRecord as TextureSetRecord
    from .voli import VolumetricLightingRecord as VolumetricLightingRecord
    from .vtyp import VoiceTypeRecord as VoiceTypeRecord
    from .watr import WaterRecord as WaterRecord
    from .weap import WeaponRecord as WeaponRecord
    from .woop import WordOfPowerRecord as WordOfPowerRecord
    from .wrld import WorldspaceRecord as WorldspaceRecord
    from .wthr import WeatherRecord as WeatherRecord

_EXPORTS: dict[str, str] = {
    "AcousticSpaceRecord": "aspc",
    "ActionRecord": "aact",
    "ActivatorRecord": "acti",
    "ActorValueInformationRecord": "avif",
    "AddonNodeRecord": "addn",
    "AlchemicalApparatusRecord": "appa",
    "AmmunitionRecord": "ammo",
    "AnimatedObjectRecord": "anio",
    "ArmorAddonRecord": "arma",
    "ArmorRecord": "armo",
    "ArtObjectRecord": "arto",
    "AssociationTypeRecord": "astp",
    "BodyPartDataRecord": "bptd",
    "BookRecord": "book",
    "CameraPathRecord": "cpth",
    "CameraShotRecord": "cams",
    "CellRecord": "cell",
    "ClassValueRecord": "clas",
    "CldcRecord": "cldc",
    "ClimateRecord": "clmt",
    "CollisionLayerRecord": "coll",
    "ColorRecord": "clfm",
    "CombatStyleRecord": "csty",
    "ConstructibleObjectRecord": "cobj",
    "ContainerRecord": "cont",
    "DebrisRecord": "debr",
    "DefaultObjectManagerRecord": "dobj",
    "DialogBranchRecord": "dlbr",
    "DialogTopicRecord": "dial",
    "DialogViewRecord": "dlvw",
    "DoorRecord": "door",
    "DualCastDataRecord": "dual",
    "EffectShaderRecord": "efsh",
    "EncounterZoneRecord": "eczn",
    "EquipTypeRecord": "equp",
    "ExplosionRecord": "expl",
    "EyesRecord": "eyes",
    "FactionRecord": "fact",
    "FloraRecord": "flor",
    "FootstepRecord": "fstp",
    "FootstepSetRecord": "fsts",
    "FormIdListRecord": "flst",
    "FurnitureRecord": "furn",
    "GameSettingRecord": "gmst",
    "GlobalValueRecord": "glob",
    "GrassRecord": "gras",
    "HairRecord": "hair",
    "HazardRecord": "hazd",
    "HeadPartRecord": "hdpt",
    "IdleAnimationRecord": "idle",
    "IdleMarkerRecord": "idlm",
    "ImageSpaceAdapterRecord": "imad",
    "ImageSpaceRecord": "imgs",
    "ImpactDataSetRecord": "ipds",
    "ImpactRecord": "ipct",
    "InfoRecord": "info",
    "IngestibleRecord": "alch",
    "IngredientRecord": "ingr",
    "KeyRecord": "keym",
    "KeywordRecord": "kywd",
    "LandscapeRecord": "land",
    "LandscapeTextureRecord": "ltex",
    "LensFlareRecord": "lens",
    "LeveledItemRecord": "lvli",
    "LeveledNpcRecord": "lvln",
    "LeveledSpellRecord": "lvsp",
    "LightRecord": "ligh",
    "LightingTemplateRecord": "lgtm",
    "LoadScreenRecord": "lscr",
    "LocationRecord": "lctn",
    "LocationReferenceTypeRecord": "lcrt",
    "MagicEffectRecord": "mgef",
    "MainFileHeaderRecord": "tes4",
    "MaterialObjectRecord": "mato",
    "MaterialTypeRecord": "matt",
    "MessageRecord": "mesg",
    "MiscItemRecord": "misc",
    "MoveableStaticRecord": "mstt",
    "MovementTypeRecord": "movt",
    "MusicTrackRecord": "must",
    "MusicTypeRecord": "musc",
    "NavmeshInfoMapRecord": "navi",
    "NavmeshRecord": "navm",
    "NpcRecord": "npc",
    "ObjectEffectRecord": "ench",
    "OutfitRecord": "otft",
    "PackageRecord": "pack",
    "PerkRecord": "perk",
    "PlacedArrowRecord": "parw",
    "PlacedBarrierRecord": "pbar",
    "PlacedBeamRecord": "pbea",
    "PlacedConeVoiceRecord": "pcon",
    "PlacedFlameRecord": "pfla",
    "PlacedHazardRecord": "phzd",
    "PlacedMissileRecord": "pmis",
    "PlacedNpcRecord": "achr",
    "PlacedObjectRecord": "refr",
    "PlacedProjectileRecord": "pgre",
    "PlayerReferenceRecord": "plyr",
    "ProjectileRecord": "proj",
    "PwatRecord": "pwat",
    "QuestRecord": "qust",
    "RaceRecord": "race",
    "RegionRecord": "regn",
    "RelationshipRecord": "rela",
    "ReverbParametersRecord": "revb",
    "RgdlRecord": "rgdl",
    "SceneRecord": "scen",
    "ScptRecord": "scpt",
    "ScrollRecord": "scrl",
    "ShaderParticleGeometryRecord": "spgd",
    "ShoutRecord": "shou",
    "SoulGemRecord": "slgm",
    "SoundCategoryRecord": "snct",
    "SoundDescriptorRecord": "sndr",
    "SoundMarkerRecord": "soun",
    "SoundOutputModelRecord": "sopm",
    "SpellRecord": "spel",
    "StaticCollectionRecord": "scol",
    "StaticRecord": "stat",
    "StoryManagerBranchNodeRecord": "smbn",
    "StoryManagerEventNodeRecord": "smen",
    "StoryManagerQuestNodeRecord": "smqn",
    "TalkingActivatorRecord": "tact",
    "TextureSetRecord": "txst",
    "TreeRecord": "tree",
    "VisualEffectRecord": "rfct",
    "VoiceTypeRecord": "vtyp",
    "VolumetricLightingRecord": "voli",
    "WaterRecord": "watr",
    "WeaponRecord": "weap",
    "WeatherRecord": "wthr",
    "WordOfPowerRecord": "woop",
    "WorldspaceRecord": "wrld",
}

__all__ = [
    "AcousticSpaceRecord",
    "ActionRecord",
    "ActivatorRecord",
    "ActorValueInformationRecord",
    "AddonNodeRecord",
    "AlchemicalApparatusRecord",
    "AmmunitionRecord",
    "AnimatedObjectRecord",
    "ArmorAddonRecord",
    "ArmorRecord",
    "ArtObjectRecord",
    "AssociationTypeRecord",
    "BodyPartDataRecord",
    "BookRecord",
    "CameraPathRecord",
    "CameraShotRecord",
    "CellRecord",
    "ClassValueRecord",
    "CldcRecord",
    "ClimateRecord",
    "CollisionLayerRecord",
    "ColorRecord",
    "CombatStyleRecord",
    "ConstructibleObjectRecord",
    "ContainerRecord",
    "DebrisRecord",
    "DefaultObjectManagerRecord",
    "DialogBranchRecord",
    "DialogTopicRecord",
    "DialogViewRecord",
    "DoorRecord",
    "DualCastDataRecord",
    "EffectShaderRecord",
    "EncounterZoneRecord",
    "EquipTypeRecord",
    "ExplosionRecord",
    "EyesRecord",
    "FactionRecord",
    "FloraRecord",
    "FootstepRecord",
    "FootstepSetRecord",
    "FormIdListRecord",
    "FurnitureRecord",
    "GameSettingRecord",
    "GlobalValueRecord",
    "GrassRecord",
    "HairRecord",
    "HazardRecord",
    "HeadPartRecord",
    "IdleAnimationRecord",
    "IdleMarkerRecord",
    "ImageSpaceAdapterRecord",
    "ImageSpaceRecord",
    "ImpactDataSetRecord",
    "ImpactRecord",
    "InfoRecord",
    "IngestibleRecord",
    "IngredientRecord",
    "KeyRecord",
    "KeywordRecord",
    "LandscapeRecord",
    "LandscapeTextureRecord",
    "LensFlareRecord",
    "LeveledItemRecord",
    "LeveledNpcRecord",
    "LeveledSpellRecord",
    "LightRecord",
    "LightingTemplateRecord",
    "LoadScreenRecord",
    "LocationRecord",
    "LocationReferenceTypeRecord",
    "MagicEffectRecord",
    "MainFileHeaderRecord",
    "MaterialObjectRecord",
    "MaterialTypeRecord",
    "MessageRecord",
    "MiscItemRecord",
    "MoveableStaticRecord",
    "MovementTypeRecord",
    "MusicTrackRecord",
    "MusicTypeRecord",
    "NavmeshInfoMapRecord",
    "NavmeshRecord",
    "NpcRecord",
    "ObjectEffectRecord",
    "OutfitRecord",
    "PackageRecord",
    "PerkRecord",
    "PlacedArrowRecord",
    "PlacedBarrierRecord",
    "PlacedBeamRecord",
    "PlacedConeVoiceRecord",
    "PlacedFlameRecord",
    "PlacedHazardRecord",
    "PlacedMissileRecord",
    "PlacedNpcRecord",
    "PlacedObjectRecord",
    "PlacedProjectileRecord",
    "PlayerReferenceRecord",
    "ProjectileRecord",
    "PwatRecord",
    "QuestRecord",
    "RaceRecord",
    "RegionRecord",
    "RelationshipRecord",
    "ReverbParametersRecord",
    "RgdlRecord",
    "SceneRecord",
    "ScptRecord",
    "ScrollRecord",
    "ShaderParticleGeometryRecord",
    "ShoutRecord",
    "SoulGemRecord",
    "SoundCategoryRecord",
    "SoundDescriptorRecord",
    "SoundMarkerRecord",
    "SoundOutputModelRecord",
    "SpellRecord",
    "StaticCollectionRecord",
    "StaticRecord",
    "StoryManagerBranchNodeRecord",
    "StoryManagerEventNodeRecord",
    "StoryManagerQuestNodeRecord",
    "TalkingActivatorRecord",
    "TextureSetRecord",
    "TreeRecord",
    "VisualEffectRecord",
    "VoiceTypeRecord",
    "VolumetricLightingRecord",
    "WaterRecord",
    "WeaponRecord",
    "WeatherRecord",
    "WordOfPowerRecord",
    "WorldspaceRecord",
]


def __getattr__(name: str) -> object:
    """Loads only the requested record module.

    Args:
        name: Record class exported by this game package.

    Returns:
        The requested generated class.

    Raises:
        AttributeError: The class is not part of this schema.
    """

    if name not in _EXPORTS:
        raise AttributeError(name)
    module = importlib.import_module(f"{__name__}.{_EXPORTS[name]}")
    value: object = getattr(module, name)
    globals()[name] = value
    return value
