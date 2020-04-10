import json
import subprocess
import re

statistics = {}
matcher = re.compile('\d+')

# Memory usage
total_ram = subprocess.run(['sysctl', 'hw.memsize'], stdout=subprocess.PIPE).stdout.decode('utf-8')
vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
vmLines = vm.split('\n')

wired_memory = (int(matcher.search(vmLines[6]).group()) * 4096) / 1024 ** 3
free_memory = (int(matcher.search(vmLines[1]).group()) * 4096) / 1024 ** 3
active_memory = (int(matcher.search(vmLines[2]).group()) * 4096) / 1024 ** 3
inactive_memory = (int(matcher.search(vmLines[3]).group()) * 4096) / 1024 ** 3

# Used memory = wired_memory + inactive + active

statistics['ram'] = dict({
    'total_ram': int(matcher.search(total_ram).group())/1024**3,
    'used_ram': round(wired_memory+active_memory+inactive_memory, 2),
})

print(json.dumps(statistics, indent=4, sort_keys=True))
