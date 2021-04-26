import time
def day84(matrix):
    tick = time.time()
    rows = len(matrix)
    collums = len(matrix[0])
    i = 0
    islands = []
    checked = []
    for r in range(rows):
        for c in range(collums):
            if matrix[r][c] and [r, c] not in checked:
               islands.append(checkaround([r, c], [[r,c]], matrix, rows, collums))
               checked = checked + islands[-1]
               i = i + 1
    tock = time.time()
    timetook = tock - tick
    return i, islands, timetook
    

def checkaround(spot, island, matrix, rows, collums):
    r = spot[0]
    c = spot[1]
    if [r-1, c] not in island and r > 0 and matrix[r-1][c]:
         island.append([r-1, c])
         checkaround([r-1, c], island, matrix, rows, collums)
    if [r, c-1] not in island and c > 0 and  matrix[r][c-1]:
        island.append([r, c-1])
        checkaround([r, c-1], island, matrix, rows, collums)

    if [r+1, c] not in island and r < (rows-1) and matrix[r+1][c]:
        island.append([r+1, c])
        checkaround([r+1, c], island, matrix, rows, collums)

    if [r, c+1] not in island and c < (collums-1) and matrix[r][c+1]:
        island.append([r, c+1])
        checkaround([r, c+1], island, matrix, rows, collums)

    return island
