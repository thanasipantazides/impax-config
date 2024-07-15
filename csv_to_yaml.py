import yaml, sys, pandas

if __name__ == "__main__":
    if len(sys.argv) == 3:
        print("\nReading from\t", sys.argv[1])

        nancounter = 0
        data = []
        raw = pandas.read_csv(sys.argv[1], header=0)
        print(raw)
        for record in raw.iterrows():
            if not pandas.isna(record[1]["Latitude"]):
                this_data = {
                    "name":         record[1]["Name"],
                    "operator":     record[1]["Operator"],
                    "latitude":     record[1]["Latitude"],
                    "longitude":    record[1]["Longitude"],
                    "altitude":     record[1]["Altitude [m]"],
                    "elevation":    record[1]["Elevation [deg]"],
                }
                data.append(this_data)
            else:
                nancounter += 1
        
        with open(sys.argv[2], "w") as output:
            yaml.dump(data, output, default_flow_style=False)
        print("Wrote output to ", sys.argv[2], "\nFound and dropped", nancounter, "NaN rows")
        
    else:
        print("use like this:\n\t> python3 csv_to_yaml.py <input_csv_path> <output_yaml_path>")
