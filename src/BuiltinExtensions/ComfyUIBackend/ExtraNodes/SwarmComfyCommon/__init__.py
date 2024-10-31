from . import SwarmImages, SwarmInternalUtil, SwarmKSampler, SwarmMasks, SwarmTextHandling,

WEB_DIRECTORY = "./web"

NODE_CLASS_MAPPINGS = (
    SwarmImages.NODE_CLASS_MAPPINGS
    | SwarmInternalUtil.NODE_CLASS_MAPPINGS
    | SwarmKSampler.NODE_CLASS_MAPPINGS
    | SwarmMasks.NODE_CLASS_MAPPINGS
    | SwarmTextHandling.NODE_CLASS_MAPPINGS
)
