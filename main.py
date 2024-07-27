import sys
import subprocess


def main():
    args_len = len(sys.argv) - 1
    if args_len <= 2:
        print("Usage: <in_dir> <out_file> song1 song2 song3...")
        return
    in_dir = sys.argv[1]
    out_file = sys.argv[2]
    #not verifying, too lazy
    songs_list = sys.argv[3:]
    
    res = subprocess.run(["find", in_dir], stdout=subprocess.PIPE)
    lines = []
    songs_path_list = []
    
    lines = res.stdout.decode("utf-8").split("\n")

    #print(lines)
    for i in range(len(songs_list)):
        song = songs_list[i]
        found = []
        for line in lines:
            
            if not song in line.split("/")[-1].lower():
                continue
            found.append(line)
        if len(found) == 0:
            print(f"Unable to find {song}. Skipping.")
            continue
        idx = 0
        if len(found) > 1:
            print(f"Ambiguous song name \"{song}\". Input index to choose which song you want included. ")
            for j in range(len(found)):
                print(f"{j}: {found[j].split("/")[-1]}")
            input("Index: ")
        song_chosen = found[idx] 
        songs_path_list.append(song_chosen)
    
    with open(out_file, "w+") as f:
        for l in songs_path_list:
            f.write(l + "\n")

main()