import setuptools

setuptools.setup(
    name="northstar_epe_planner",
    version="0.0.1",
    description="Package to help interact with Northstar's EPE Planner",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
)
