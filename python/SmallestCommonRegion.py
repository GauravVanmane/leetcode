def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
    dict_region = {}
    for region in regions:
        for j in region[1:]:
            dict_region[j] = region[0]
    parent =set()
    parent.add(region1)
    
    while region1 in dict_region:
        region1 = dict_region[region1]
        parent.add(region1)
        
    while region2 not in parent:
        region2 = dict_region[region2]
    return region2