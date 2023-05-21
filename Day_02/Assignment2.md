<h2>Problem Statment : To implement the following methods in project that we built </h2>
<ul>
  <li> Search by place</li>
  <li> Search by warranty </li>
  <li> Use Stream API for the methods</li>
</ul>

<h3> Search by place </h3>

```java 
public List<Products> getProductWithPlace(String pl) {
    List<Products> prods = new ArrayList();
    pl = pl.toLowerCase();

    for (Products p : products) {
        String place = p.getPlace().toLowerCase();

        if (place.contains(pl)) {
            prods.add(p);
        }
    }

    return prods;
}
```
Now let us see what is happening here, the method will return a list of all the products with the place name that we will have given as input. Then inside the method we are initializing an empty list called prods, then we are creating a variable pl which will store the name of the place but in lowercase. This is done to make the searching of names easier as the contains method is `case sensitive`.

After that we are using an `enhanced for loop` (the definition of which i have given in my notes) and we are iterating through all the products that we have in our list like database and we are inserting all the products that match the value present in the variable pl.

In the last step we are returning the list containing our result and thats why the return type is List.

<b>Note :I was a bit confused if Navin sir said to find the products out of warranty or by their warranty so I have done both the methods </b>

<h3> Searching Products out of Warranty</h3>

```java
 public List<Products> getProuctsOutofWarranty(int w) {
   List<Products> prods = new ArrayList();
   for (Products p : products) {
     if (p.getWarranty() > w) {
       prods.add(p);
     }
   }
   return prods;
    }
```
In this method what we are doing is we will give the input in terms of the warranty which is of integer type. Then we will initialize a list called prods where we will store our result.

Then we use an enhanced for loop to iterate through all the products and find all the products whose warranty has expired that means all the products whose warranty is greater than the number that we gave as input.

We then add it to the prods list and return it.


<h3> Using Stream API for the methods</h3>
I have provided a detailed explanation of stream API which i have posted on Linkedin. Check that out for more details. To provide a very general understanding of what every method is doing is that
<ul>
  <li> first we are calling the stream method </li>
  <li> then we are using the filter method which takes in a lambda expression which is basically the condition that we have  </li>
  <li> then we are using a collect method which will uses Collector.toList() to convert the result into a list </li> 

<h4> Finding product with product name</h4>

```java
public List<Products> getProducts(String name){
        return products.stream()
                .filter(p -> p.getName().toLowerCase().contains(name.toLowerCase()))
                .collect(Collectors.toList());
    }
```

<h4> Finding product with text</h4>

```java
 public List<Products> getProductswithText(String t) {
        return products.stream()
                .filter(p -> p.getName().toLowerCase().contains(t.toLowerCase()) || p.getType().toLowerCase().contains(t.toLowerCase()) || p.getPlace().toLowerCase().contains(t.toLowerCase()))
                .collect(Collectors.toList());
    }
```

<h4> Getting all the Products</h4>

```java
public List<Products> getallProducts() {
        return products.stream()
                .collect(Collectors.toList());
    }
```
<h4> Getting Products by Warranty</h4>

```java
 public List<Products> getProductsByWarranty(int w) {
        return products.stream()
                .filter(p -> p.getWarranty() == w)
                .collect(Collectors.toList());
    }
```

<h4> Getting products out of Warranty</h4>

```java
   public List<Products> getProductsOutOfWarranty(int w) {
        return products.stream()
                .filter(p -> p.getWarranty() > w)
                .collect(Collectors.toList());
    }
```





