import os
os.system('curl -sL https://sentry.io/get-cli/ | bash')

def process_sentry(project, directory):
    for r, d, f in os.walk(directory):
        for file in f:
            if 'lib' in file or 'obs' in file or '.so' in file or '.dylib' in file:
                path = os.path.join(directory, file)
                os.system("dsymutil " + path)
                os.system("sentry-cli --auth-token ${SENTRY_AUTH_TOKEN} upload-dif --org streamlabs-obs --project " + project + " " + path + ".dSYM/Contents/Resources/DWARF/" + file)

# # Upload client debug files
process_sentry('obs-client', os.path.join(os.environ['PWD'], os.environ['SLBUILDDIRECTORY'], 'obs-client', os.environ['BUILDCONFIG']))
# # Upload server debug files
process_sentry('obs-server', os.path.join(os.environ['PWD'], os.environ['SLBUILDDIRECTORY'], 'obs-server', os.environ['BUILDCONFIG']))

# # Upload client debug files
process_sentry('obs-client', os.path.join(os.environ['PWD'], os.environ['SLBUILDDIRECTORY'], 'obs-client-preview', os.environ['BUILDCONFIG']))
# # Upload server debug files
process_sentry('obs-server', os.path.join(os.environ['PWD'], os.environ['SLBUILDDIRECTORY'], 'obs-server-preview', os.environ['BUILDCONFIG']))