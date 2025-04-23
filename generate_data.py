import os
import sys
import subprocess


def run_script(script_path):
    print(f"\nRunning script: {os.path.basename(script_path)}")
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(f"Error in {script_path}:", result.stderr)
        sys.exit(result.returncode)
    print(result.stdout)


def main():
    gen_dir = os.path.join(os.path.dirname(__file__), 'generator')

    if not os.path.isdir(gen_dir):
        print(f"Generator directory not found: {gen_dir}")
        sys.exit(1)

    # Hardcoded execution order
    scripts = [
        'authors_generator.py',
        'journals_generator.py',
        'keywords_generator.py',
        'papers_generator.py',
        'reviews_generator.py',
        'conferences_generator.py',
        'volumes_generator.py',
        'conference_editions_generator.py',
        'venues_generator.py',
        'conn_authorship.py',
        'conn_paper_cities.py',
        'conn_paper_conf_journal.py',
        'conn_paper_keywords.py',
        'conn_relationships.py'
    ]

    print(f"Executing {len(scripts)} generators in hardcoded order...\n")
    for script in scripts:
        script_path = os.path.join(gen_dir, script)
        if not os.path.isfile(script_path):
            print(f"Warning: generator script not found: {script_path}")
            continue
        
        # Simply run each script
        run_script(script_path)

    print("\nAll scripts have completed successfully.")


if __name__ == '__main__':
    main()