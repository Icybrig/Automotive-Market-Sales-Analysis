import subprocess

def run_script(script_path):
    print(f" Running {script_path} ...")
    subprocess.run(["python", script_path], check=True)
    print(f"{script_path} has been executed！\n")

def main():
    try:
        run_script("src/clean_data.py")
        
        run_script("db/init_db.py")
        
        run_script("src/export_to_db.py")
        
        run_script("src/run_sql_queries.py")
        
        run_script("visualization/plot_analysis.py")

        print("All scripts has been executed！")

    except subprocess.CalledProcessError as error:
        print(f" mistake in executing {error.cmd}！")
    except Exception as e:
        print(f"❌ unknown: {error}")

if __name__ == "__main__":
    main()