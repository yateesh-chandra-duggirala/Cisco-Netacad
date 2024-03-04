import extra_package.good.beta              # importing module from the package.
import extra_package.good.alpha as alpha    # Aliasing and using it instead of writing.
from extra_package.iota import funIota      # We can import the function from the module.

print("Alpha function Content:",alpha.funAlpha())
print("Iota function Content:", funIota())
print("Beta Function Content:", extra_package.good.beta.funBeta())