from distutils.core import setup
setup(
  name='Binary Classification Metrics',        
  packages = ['Binary Classification Metrics'],   
  version = '0.0.1',      
  license='MIT',        
  description='This package contains various binary classification metric methods.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),   
  author = 'Varun V',                  
  author_email = 'varunofficial99@gmail.com',      
  url = 'https://github.com/VarunV991/Binary-Classification-Metrics',  
  download_url = 'https://github.com/VarunV991/Binary-Classification-Metrics/archive/v0.0.1.tar.gz',   
  keywords = ['binary-classification', 'metrics'], 
  classifiers=[
    'Development Status :: 5 - Production/Stable',     
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.6',      
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)