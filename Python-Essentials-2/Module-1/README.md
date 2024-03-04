## Python Packaging Ecosystem
- Python is a very powerful instrument.
- Python is used on a regular basis to develop what they can do many completely different fields of activity.
- This means that python has become an interdisciplinary tool employed in countless applications.
- Python has turned into a leader of research on artificial intelligence.
- Data mining, one of the most promising modern scientific disciplines, utilizes Python as well. 
- Mathematicians, Psychologists, geneticists, meteorologists, linguistics - all these people already use Python
- Python was created as open-source software, and this also works as an invitation for all coders to maintain the whole python ecosystem as an open-friendly and free environment.
- To make the model work and evolve, some additional tools should be provided, tools that help the creators to publish, maintain and take care of their code.
- These same tools should help users to make use of the code, both the already existing code, and also new code appearing every day. Thanks to that, writing new code for new challenges is not like building a new house, starting at the foundations.
- To make this world go round, two basic entities have to be established and kept in motion: A centralized repository of all available software packages; and a tool allowing users to access the repository. Both of these entities already exist and can be used at any time.
- The repo we mentioned before is named PyPI (Python Package Index) and it is maintained by a workgroup named the packaging Working Group, a part of the Python Software Foundation, whose main task is to support Python developers in efficient code dissemination.
- We must point out that PyPI is not the only existing Python repository. On the contrary, there are lots of them, created for projects and led by many larger and smaller Python Communities. It is likely that someday you and your colleagues may want to create your own repos.
- Anyway, PyPI is the most important Python Repo in the world. If we modify the classic saying a little, we can state that "all Python roads lead to PyPI" and that is no exaggeration at all.

- The PyPI repo is sometimes referred to as the Cheese Shop.
- The Repo is referred to as a shop, because we go there for the same reasons you go to other shops: to fulfill your needs. If you want some cheese, you go to the chinese shop. If we want a piece of software, you go to the somewhere shop. 
- Fortunately, the analogy ends here - You do not need any money to take some software out of the repo shop.
- PyPI is completely free, and you can just pick a code and use it - you will encounter neither cashier nor security guard.
- Of Course, It doesn't absolve you from being polite and honest. You have to obey all the licensing terms, so do not forget to read them.
- OK, you say, "the shop is clear now, but what does cheese have to do with python?"
- The Cheese Shop is one of the most famous Monty Python sketches. It depicts the surrealist adventure of an Englishman trying to buy some cheese.
- Unfortunately, the shop he visits has no cheese in stock at all.
- Of course, it is meant to be ironic. As you already know, PyPI has lots of software in stock and it is available 24/7. it is fully entitled to identify itself as Ye International Python Software Emporium.
- PIP means "Pip Installs Packages"

## Dependencies :
- Dependency is a Phenomenon that appears every time you are going to use a piece of software that relies on other software.
- The process of ardulously fulfilling all the subsequent requirements has its own name, and it is called dependency hell.
- Pip can discover, identify and resolve all dependencies by avoiding any unnecessary downloads and reinstalls.
- We can use PIP help, pip help operation, pip help install, pip list.
- pip show package_name for getting info about package

## Pip Activites :
pip help operation – shows a brief description of pip;
pip list – shows a list of the currently installed packages;
pip show package_name – shows package_name info including the package's dependencies;
pip search anystring – searches through PyPI directories in order to find packages whose names contain anystring;
pip install name – installs name system-wide (expect problems when you don't have administrative rights);
pip install --user name – installs name for you only; no other platform user will be able to use it;
pip install -U name – updates a previously installed package;
pip uninstall name – uninstalls a previously installed package.