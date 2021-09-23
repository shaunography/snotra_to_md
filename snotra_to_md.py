import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser(description="Snotra to Mark Down")
    parser.add_argument(
        "--output-dir",
        help="output dir",
        dest="o",
        required=True,
        metavar="output_dir"
    ),
    parser.add_argument(
        "--results-file",
        help="Snotra results JSON file",
        dest="i",
        required=True,
        metavar="results_file"
    ),
    args = parser.parse_args()

    results_file = args.i
    
    with open(results_file,'r') as f:
        results = json.load(f)

    try:
        filename = os.path.split(results_file)[1].split(".")[0]
    except IndexError:
        filename = "results"
    
    ### All
    file_path = os.path.join(args.o, "{}.md".format(filename))
    with open(file_path, 'w') as f:
        
        f.write("# Account Details\n")
        f.write("\n## ID\n")
        f.write(results["account"])
        f.write("\n\n## User\n")
        f.write(results["user"])
        f.write("\n\n## DateTime\n")
        f.write(results["datetime"])
        f.write("\n---")

        f.write("\n\n# Findings")
        for finding in results["findings"]:
            
            f.write("\n\n## ")
            f.write(finding["name"])

            f.write("\n\n### ID\n")
            f.write(finding["id"])

            f.write("\n### Service\n")
            f.write(finding["service"])

            f.write("\n### REF\n")
            f.write(finding["ref"])
            
            f.write("\n### Compliance\n")
            f.write(finding["compliance"])
            
            f.write("\n### Level\n")
            f.write(str(finding["level"]))

            f.write("\n\n### CVSS Score\n")
            f.write(finding["cvss_score"])

            f.write("\n### CVSS Vector\n")
            f.write(finding["cvss_vector"])
            
            f.write("\n### Impact\n")
            f.write(finding["impact"])
            
            f.write("\n### Probability\n")
            f.write(finding["probability"])            
            
            f.write("\n### Pass/Fail\n")
            f.write(finding["pass_fail"])
            
            f.write("\n\n### Affected\n")
            f.write(finding["affected"])
            
            f.write("\n\n### Description\n")
            f.write(finding["description"])
            
            f.write("\n\n### Remediation\n")
            f.write(finding["remediation"])

            f.write("\n\n### Analysis\n")
            f.write(finding["analysis"])

if __name__ == '__main__':
    main()
