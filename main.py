import subprocess

print('Running mvn test..')
print(subprocess.getoutput('mvn test'))
print('\nGetting coverage..')
print(subprocess.getoutput('uv run server.py get_coverage'))

