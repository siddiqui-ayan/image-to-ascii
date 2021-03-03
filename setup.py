
from distutils.core import setup
setup(
  name = 'image_to_ascii',       
  packages = ['image_to_ascii'], 
  version = '0.2',      
  license='MIT',
  description = 'A simple python library to convert images to ASCII art',
  long_description="README.md",
  author = 'Aypro',
  author_email = 'ayprogaming1@gmail.com',
  url = 'https://github.com/aypro-droid/image-to-ascii',
  download_url = 'https://github.com/aypro-droid/image-to-ascii/archive/v_01.tar.gz',
  keywords = ['IMAGE','TO','ASCII','ASCII', 'ART'],
  install_requires=[
          'pillow'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
