"""
Flask-Danger
-------------

Flask extension for Danger (https://usedanger.com). Provides helpers to render
the Danger widget on auth forms and to send server-side events.
"""
from setuptools import setup


setup(
    name="Flask-Danger",
    version="1.0",
    url="https://github.com/danger-org/flask-danger",
    license="MIT",
    author="Danger",
    author_email="support@usedanger.com",
    description="Flask extension for Danger",
    long_description=__doc__,
    py_modules=["flask_danger"],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)