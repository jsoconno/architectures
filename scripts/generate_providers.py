import os
from pathlib import Path

def format_text(text):
    return text.replace("-", " ").title().replace(" ", "")

root_dir = os.path.dirname(os.getcwd())
icons_dir = os.path.join(root_dir, "icons")

providers = os.listdir(icons_dir)

for provider in providers:
    for subdir, dirs, files in os.walk(os.path.join(icons_dir, provider)):
        if files:
            service_type = os.path.split(subdir)[1]

            provider_dir = os.path.join(root_dir, "architectures", "providers", provider)
            if not os.path.exists(provider_dir):
                os.mkdir(provider_dir)

            service_file = os.path.join(provider_dir, service_type) + ".py"

            provider_fmt = format_text(provider)
            service_type_fmt = format_text(service_type)
            
            with open(service_file, "w+") as f:
                # Create service type class
                f.write(f'# Do not modify this file directly. It is auto-generated with Python.\n\n')
                f.write(f'from architectures.providers import _{provider_fmt}\n\n')
                f.write(f'class _{service_type_fmt}(_{provider_fmt}):\n')
                f.write(f'\t_service_type = \"{service_type}\"\n')
                f.write(f'\t_icon_dir = \"icons/{provider}/{service_type}\"\n\n')

    # each image is code: administrative-unit.png

            for service in files:
                raw_service = service.split(".")[0]
                service_fmt = format_text(raw_service)
                
                with open(service_file, 'a+', newline='') as f:
                    # Create service type class
                    f.write(f'class {service_fmt}(_{service_type_fmt}):\n')
                    f.write(f'\t_icon = \"{service}\"\n')
                    f.write(f'\t_default_label = "{raw_service.replace("-", " ").title()}"\n\n')
