def wordcount(filename):
    with open(filename, 'r') as file:
        counts = {}
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;"\'()[]{}')
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

    # Sort by frequency
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    for word, freq in sorted_counts[:10]:
        print(word, freq)

def main():
    try:
        wordcount("input.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()