# Introduction
## Description

## Examples
### With [REST](./rest.md)
* Uses Web, JPA, J2
    * H2 -- an in memory SQL style database
    * JPA -- to interface? with H2
        * JPA can create object for store via object classes
        * @Id -- primary id 
        * @GeneratedValue -- auto gen value
    * Spring MVC (Web?) is used to access remotely
* Runs without the use of xml; Spring boot can directly use the following to run server:
```
public static void main(String[] args) {
    SpringApplication.run(AccessingDataJpaApplication.class, args);
}
```
* Can create a jar for deployment if so desired (depends on build systems)
