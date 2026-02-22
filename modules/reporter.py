from datetime import datetime
import os

def generate_report(target, data_dict):
    """
    Saves the aggregated OSINT data into a timestamped text file.
    """
    # Create 'reports' directory if it doesn't exist
    if not os.path.exists('reports'):
        os.makedirs('reports')

    # Generate a filename with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/NazarBOT_{target}_{timestamp}.txt"

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"{'='*30}\n")
            f.write(f" NAZARBOT OSINT REPORT\n")
            f.write(f" Target: {target}\n")
            f.write(f" Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*30}\n\n")

            # Iterate through each module's results
            for module, results in data_dict.items():
                f.write(f"--- [ {module.upper()} ] ---\n")
                if isinstance(results, list):
                    for item in results:
                        f.write(f"[+] {item}\n")
                elif isinstance(results, dict):
                    for key, val in results.items():
                        f.write(f"[+] {key}: {val}\n")
                else:
                    f.write(f"[+] {results}\n")
                f.write("\n")

        print(f"\n[!] NazarBOT: Report saved successfully to {filename}")
        return filename
    except Exception as e:
        print(f"[!] Error generating report: {e}")
        return None