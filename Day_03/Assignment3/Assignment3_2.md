<h2> Problem Statement : To Implement all the methods in the project using JPA repository and Spring Framework</h2>

So basically there are Three files 
<ul>
  <li> Product Service.java</li>
  <li> ProductDB.java</li>
  <li>ProductSpringApplication.java</li>
</ul>


<h3> ProductDB.java </h3>

```java

@Repository
public interface ProductDB extends JpaRepository<Product, Integer> {
    List<Product> findAllByNameContainingIgnoreCase(String searchText);
    List<Product> findAllByPlaceContainingIgnoreCase(String place);

    List<Product> findAllProductsOutOfWarranty(int w);

    List<Product> findAllProductsByWarranty(int w);
}
```
1. List<Product> findAllByNameContainingIgnoreCase(String searchText): This method is used to search for products in the database whose names contain a specific text. The searchText parameter represents the text to search for. The search is case-insensitive, meaning that it will match products regardless of the letter casing. The method returns a list of Product objects that match the search criteria.

2. List<Product> findAllByPlaceContainingIgnoreCase(String place): This method is similar to the previous one but searches for products based on the place associated with them. It takes a place parameter representing the place to search for, and returns a list of Product objects whose place contains the specified text. Again, the search is case-insensitive.

3. List<Product> findAllProductsOutOfWarranty(int w): This method is used to retrieve all products from the database that are out of warranty. It takes an int parameter w, which likely represents the number of years since the product's purchase date. The method returns a list of Product objects that are no longer covered by warranty.

4. List<Product> findAllProductsByWarranty(int w): This method retrieves all products from the database that have a specific warranty duration. The w parameter represents the warranty duration in years. The method returns a list of Product objects that have the specified warranty duration.

<h4> ProductService.java </h4>

```java
@Component
public class ProductService {
    @Autowired
    ProductDB db;
    public List<Product> getAllProducts(){
    return db.findAll();
    }

    public List<Product> getProductByText(String t){
    return db.findAllByNameContainingIgnoreCase(t);
    }

    public List<Product> getProductByPlace(String pl){
    return db.findAllByPlaceContainingIgnoreCase(pl);
    }

    public List<Product> getProductOutOfWarranty(int w){
    return db.findAllProductsOutOfWarranty(w);
    }

    public List<Product> getProductByWarranty(int w){
    return db.findAllProductsByWarranty(w);
    }
}
```
The ProductService class acts as a bridge between the controller layer and the ProductDB data access layer. It provides methods to perform various operations on products:

getAllProducts(): Retrieves all products from the database.
getProductByText(t): Searches for products whose names contain a specific text (t).
getProductByPlace(pl): Searches for products associated with a specific place (pl).
getProductOutOfWarranty(w): Retrieves products that are out of warranty (based on a specified number of years w).
getProductByWarranty(w): Retrieves products with a specific warranty duration (w).

<h3> ProductSpringApplication.java</h3>

```java
@SpringBootApplication
public class ProductSpringApplication {

	public static void main(String[] args) {
		ApplicationContext context = SpringApplication.run(ProductSpringApplication.class, args);

		ProductService ps = context.getBean(ProductService.class);

		List<Product> products = ps.getAllProducts();
		System.out.println("All Products: ");
		for (Product p : products) {
			System.out.println(p);
		}

		System.out.println("Products with Text: ");
		List<Product> productsWithText = ps.getProductByText("a");
		for (Product p : productsWithText) {
			System.out.println(p);
		}

		System.out.println("Products with Place: ");
		List<Product> productsWithPlace = ps.getProductByPlace("a");
		for (Product p : productsWithPlace) {
			System.out.println(p);
		}

		System.out.println("Products with Warranty: ");
		List<Product> productsWithWarranty = ps.getProductByWarranty(2);
		for (Product p : productsWithWarranty) {
			System.out.println(p);
		}

		System.out.println("Products out of Warranty: ");
		List<Product> productsOutOfWarranty = ps.getProductOutOfWarranty(1);
		for (Product p : productsOutOfWarranty) {
			System.out.println(p);
		}


	}

}
```
  The provided code represents a Java application entry point, ProductSpringApplication, that utilizes the Spring Boot framework. Here is a description of the code:

1. @SpringBootApplication: This annotation indicates that this class is the entry point of a Spring Boot application. 

2. public static void main(String[] args): This is the main method of the application. It serves as the starting point when the application is executed.

3. ApplicationContext context = SpringApplication.run(ProductSpringApplication.class, args): This line creates an instance of the Spring ApplicationContext by running the ProductSpringApplication class. It starts the Spring Boot application and initializes the Spring container.

