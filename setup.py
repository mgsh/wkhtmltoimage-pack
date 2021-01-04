from setuptools import setup

setup(
    name='wkhtmltoimage-pack',
    version='0.12.5',
    url='https://github.com/mgsh/wkhtmltoimage-pack',
    author='Magesh Dhasayyan',
    license='MIT',
    data_files=[('bin', ['bin/wkhtmltoimage-pack'])],
    description='wkhtmltoimage 0.12.5 for Python',
    long_description=open('README.rst').read(),
    keywords='wkhtmltoimage paas',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe=False
)
