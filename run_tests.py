import subprocess
import sys

print("=" * 80)
print("URUCHAMIANIE TESTÓW AKCEPTACYJNYCH - BOULDER GYM")
print("=" * 80)
print()

result = subprocess.run(
    ['behave', '--format=progress', '--summary', '--no-capture'],
    capture_output=False,
    text=True
)

print()
print("=" * 80)
print(f"WYNIK: {'SUKCES' if result.returncode == 0 else 'NIEPOWODZENIE'}")
print("=" * 80)

sys.exit(result.returncode)
