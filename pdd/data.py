import os

FILENAME = os.path.join(os.path.dirname(__file__), "pdd.txt")

def load_data():
    pdd = []
    with open(FILENAME, 'r') as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) == 4:
                    pdd.append([parts[0], parts[1], int(parts[2]), int(parts[3])])
    return pdd

                    
def save_data(pdd):
     with open(FILENAME, 'w') as f:
          for p in pdd:
               f.write(f"{p[0]};{p[1]};{p[2]};{p[3]}")