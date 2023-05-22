<h2> Problem Statement : To Implement the Methods in the Project using the JDBC interface and with a Postgres Database</h2>

<h3> Getting all the products in the Database</h3>

```java
List<Products> products = ps.getAllProducts();
System.out.println("All Products: ");
for (Products p : products) {
   System.out.println(p);
        }
  ```

So what is happening over here is we are using the product service class method called `getAllProducts()` and this method takes no arguments in the `ProductService` class the method looks like 

```java
public List<Products> getAllProducts() throws SQLException {
        List<Products> all_products = db.getAll();
        return all_products;
    }
```

the method is of type list which means it will return a list of items this list of items will come from the `db` object which has a method `getAll()` which will look like,

```java
 public List<Products> getAll() {
        String query = "SELECT * FROM product";
        try {
            PreparedStatement stmt = conn.prepareStatement(query);
            ResultSet rs = stmt.executeQuery();
            List<Products> products = new ArrayList<>();
            while (rs.next()) {
                Products p = new Products();
                p.setName(rs.getString("name"));
                p.setType(rs.getString("type"));
                p.setPlace(rs.getString("place"));
                p.setWarranty(rs.getInt("warranty"));
                products.add(p);
            }
            return products;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
```

now from here the query is executed and all the products are added from a resultset to this a list called products and it is returned.

<h3>Getting the product with text</h3>

```java
List<Products> products_by_text = ps.getProductWithText("Apple");
        System.out.println("Products by text: ");
        for (Products p : products_by_text) {
            System.out.println(p);
        }
```
Here we search for all those products which have that particular text that we give as an input, 

Here also the service method does not know anything about the database and only invokes the method as shown below 

```java
   public List<Products> getProductWithText(String t) {
        List<Products> products_by_text = db.getProdByText(t);
        return products_by_text;
    }
```

No this will invoke the `getProdByText()` function which is prosent in `ProductDB` class
```java
   public List<Products> getProdByText(String t) {
        String query = "SELECT * FROM product WHERE name LIKE ?";
        try {
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setString(1, "%" + t + "%");
            ResultSet rs = stmt.executeQuery();
            List<Products> products = new ArrayList<>();
            while (rs.next()) {
                Products p = new Products();
                p.setName(rs.getString("name"));
                p.setType(rs.getString("type"));
                p.setPlace(rs.getString("place"));
                p.setWarranty(rs.getInt("warranty"));
                products.add(p);
            }
            return products;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

    }
```

<b> Note: All the methods from now have a similar explanantion on there will be change in the method names, I hope you have understood the program flow </b>


<h3> Getting Product name with place</h3>

<h4> In the `Main` class</h4>

```java
  List<Products> products_by_place = ps.getProductWithPlace("Red Table");
        System.out.println("Products by place: ");
        for (Products p : products_by_place) {
            System.out.println(p);
        }
 ```

<h4> In the `ProductsService class` </h4>

```java
public List<Products> getProductWithPlace(String pl) {
        List<Products> products_by_place = db.getProdByPlace(pl);
        return products_by_place;
    }
```

<h4> In the `ProductsDB` class</h4>

```java
public List<Products> getProdByPlace(String pl){
        String query = "SELECT * FROM product WHERE place LIKE ?";
        try {
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setString(1, "%" + pl + "%");
            ResultSet rs = stmt.executeQuery();
            List<Products> products = new ArrayList<>();
            while (rs.next()) {
                Products p = new Products();
                p.setName(rs.getString("name"));
                p.setType(rs.getString("type"));
                p.setPlace(rs.getString("place"));
                p.setWarranty(rs.getInt("warranty"));
                products.add(p);
            }
            return products;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
```
<h3> Getting Products out of Warranty </h3>

<h4> In the `Main` class</h4>

```java
  List<Products> product_out_of_warranty = ps.getProuctsOutofWarranty(3);
        System.out.println("Products out of warranty: ");
        for (Products p : product_out_of_warranty) {
            System.out.println(p);
        }
 ```

<h4> In the `ProductsService class` </h4>

```java
public List<Products> getProuctsOutofWarranty(int w) {
        List<Products> product_out_of_warranty = db.getProdOutOfWarranty(w);
        return product_out_of_warranty;
    }
```

<h4> In the `ProductsDB` class</h4>

```java
    public List<Products> getProdOutOfWarranty(int w) {
        String query = "SELECT * FROM product WHERE warranty > ?";
        try {
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setInt(1, w);
            ResultSet rs = stmt.executeQuery();
            List<Products> products = new ArrayList<>();
            while (rs.next()) {
                Products p = new Products();
                p.setName(rs.getString("name"));
                p.setType(rs.getString("type"));
                p.setPlace(rs.getString("place"));
                p.setWarranty(rs.getInt("warranty"));
                products.add(p);
            }
            return products;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

```

<h3> Getting Products by warranty</h3>

<h4> In the `Main` class</h4>

```java
 List<Products> products_by_warranty = ps.getProductsbyWarranty(3);
        System.out.println("Products by warranty: ");
        for (Products p : products_by_warranty) {
            System.out.println(p);
        }
 ```

<h4> In the `ProductsService class` </h4>

```java
 public List<Products> getProductsbyWarranty(int w) {
        List<Products> products_by_warranty = db.getProdByWarranty(w);
        return products_by_warranty;
    }
```

<h4> In the `ProductsDB` class</h4>

```java
public List<Products> getProdByWarranty(int w) {
        String query = "SELECT * FROM product WHERE warranty = ?";
        try {
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setInt(1, w);
            ResultSet rs = stmt.executeQuery();
            List<Products> products = new ArrayList<>();
            while (rs.next()) {
                Products p = new Products();
                p.setName(rs.getString("name"));
                p.setType(rs.getString("type"));
                p.setPlace(rs.getString("place"));
                p.setWarranty(rs.getInt("warranty"));
                products.add(p);
            }
            return products;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
```






  
  
 
