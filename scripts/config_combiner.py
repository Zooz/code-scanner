#!/usr/bin/python3

import yaml
import glob


class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)

print('Started config combiner python scrip')

sarifFiles = glob.glob('semgrep_rules/*')
allRules = []

for scanConfig in sarifFiles:
    f = open(scanConfig, 'r')
    scanConfigData = yaml.safe_load(f)
    allRules += scanConfigData['rules']

newConfig = {'rules': allRules}
outFile = open('semgrep_rules/semgrepRulles.yml', 'w')
outFile.write(yaml.dump(newConfig, Dumper=MyDumper, default_flow_style=False))
outFile.close()

print('Finished config combiner python scrip')