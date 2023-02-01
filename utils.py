class Utils:
    
    
    @staticmethod
    def get_child_tiles(parent_tile):
        childX = parent_tile[0] * 2
        childY = parent_tile[1] * 2
        childZoom = parent_tile[2] + 1
        return [
            [childX, childY, childZoom], [childX+1, childY, childZoom],
            [childX, childY+1, childZoom], [childX+1, childY+1, childZoom]
        ]
    
    
    @staticmethod
    def get_area_tiles(parent_tiles):
        
        child_area_tiles = []
        for tile in parent_tiles:
            child_tiles = Utils.get_child_tiles(tile)
            for child in child_tiles:
                child_area_tiles.append(child)
        return child_area_tiles
    
    
    @staticmethod
    def get_successor_tiles(current_area_zoom_parent_tiles):
        current_zoom = current_area_zoom_parent_tiles[0][2]
        successor_tiles = [current_area_zoom_parent_tiles]
        for zoom in range(current_zoom, 9):
            child_tiles = Utils.get_area_tiles(current_area_zoom_parent_tiles)
            successor_tiles.append(child_tiles)
            current_area_zoom_parent_tiles = child_tiles
        return successor_tiles


if __name__ == '__main__':
    parent_tiles = [[0,0,0]]
    successors = Utils.get_successor_tiles(parent_tiles)
    
    zoom =  0