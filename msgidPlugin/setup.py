from setuptools import setup, find_packages

setup(
    name='Jasmin msgid plugin',
    version="0.1",
    author="Jookies LTD",
    author_email="jasmin@jookies.net",
    url="http://www.jasminsms.com",
    license="Apache v2.0",
    description="Msg id customization plugin for Jasmin SMS Gateway",
    keywords=['jasmin', 'sms', 'messaging', 'smpp', 'smsc', 'smsgateway', 'plugin'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["jasmin>=0.9.25"],
    entry_points="""
    [jasmin.content]
    msgid=msgid_plugin:get_random_unique_msgid_plugin
    """,
)
