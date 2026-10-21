import argparse
import csv
import json


def main():
    parser = argparse.ArgumentParser(description="Clean a messy CSV to JSON")
    parser.add_argument("--input", required=True, help="Path to raw CSV file")
    parser.add_argument(
        "--output", default="data/clean.json", help="Path to output JSON"
    )
    args = parser.parse_args()

    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")

    clean_data = []

    # Yahan try shuru ho raha hai
    try:
        with open(args.input, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["name"] and row["age"] and row["city"]:
                    try:
                        row["age"] = int(row["age"])
                        clean_data.append(row)
                    except ValueError:
                        pass

        with open(args.output, "w") as out_f:
            json.dump(clean_data, out_f, indent=2)

        print(f"Success! {len(clean_data)} clean rows saved to {args.output}")

    # Yahan except try ke bilkul sath (same line mein) hai
    except FileNotFoundError:
        print(f"Error: '{args.input}' file nahi mili. Path check karein!")


if __name__ == "__main__":
    main()
