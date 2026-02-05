# 2026-02-05T14:21:44.403702100
import vitis

client = vitis.create_client()
client.set_workspace(path="ECE315lab1")

platform = client.create_platform_component(name = "lab1",hw_design = "$COMPONENT_LOCATION/../lab1_hw/ece315_lab1/lab1_hw_wrapper.xsa",os = "freertos",cpu = "ps7_cortexa9_0",domain_name = "freertos_ps7_cortexa9_0")

comp = client.create_app_component(name="app_component",platform = "$COMPONENT_LOCATION/../lab1/export/lab1/lab1.xpfm",domain = "freertos_ps7_cortexa9_0")

comp = client.get_component(name="app_component")
status = comp.import_files(from_loc="", files=["C:\Users\wewanchu\School\ECE315\lab1\ECE315lab1\part1\lab1_part1.c"])

platform = client.get_component(name="lab1")
status = platform.build()

comp = client.get_component(name="app_component")
comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

comp = client.create_app_component(name="app_component_newst",platform = "$COMPONENT_LOCATION/../lab1/export/lab1/lab1.xpfm",domain = "freertos_ps7_cortexa9_0")

comp = client.get_component(name="app_component_newst")
status = comp.import_files(from_loc="", files=["C:\Users\wewanchu\Desktop\part1\lab1_part1.c", "C:\Users\wewanchu\Desktop\part1\pmodkypd.c", "C:\Users\wewanchu\Desktop\part1\pmodkypd.h"])

status = platform.build()

comp = client.get_component(name="app_component_newst")
comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

client.delete_component(name="app_component")

domain = platform.get_domain(name="freertos_ps7_cortexa9_0")

status = domain.set_config(option = "os", param = "freertos_tick_rate", value = "1000")

status = domain.regenerate()

status = platform.build()

status = platform.build()

status = platform.build()

status = platform.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

