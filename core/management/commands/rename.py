import os
from decouple import config
from django.core.management.base import BaseCommand


project_name = config('project_name')


class Command(BaseCommand):
    help = "Renames a Django project"

    def add_arguments(self, parser):
        parser.add_argument("new_project_name", type=str,
                            help="The new django project name")

    def handle(self, *args, **kwargs):
        new_project_name = kwargs["new_project_name"]

        # logic

        files_to_rename = [f"{project_name}/settings/base.py",
                           f"{project_name}/wsgi.py", "manage.py"]
        folder_to_rename = project_name

        for files in files_to_rename:
            with open(files, "r") as f:
                filedata = f.read()

            filedata = filedata.replace(project_name, new_project_name)

            with open(files, "w") as f:
                f.write(filedata)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS(
            f"PROJECT HAS BEEN SUCCESSFULLY RENAMED FROM {project_name} TO {new_project_name}"))
