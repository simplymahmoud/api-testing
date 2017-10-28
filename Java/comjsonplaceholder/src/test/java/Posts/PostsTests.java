package Posts;


import org.junit.Test;
import io.restassured.http.ContentType;

import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;



public class PostsTests {

    private static String URL = "http://jsonplaceholder.typicode.com/posts/";
    private static int id = 1;
    private static int userId = 1;
    private static String title = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit";
    private static String body = "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto";


    @Test
    public void test_View_Post() {

        given().
                when().
                get(URL + id).
                then().
                assertThat().
                statusCode(200).
                and().
                contentType(ContentType.JSON).
                and().
                header("Content-Type",equalTo("application/json; charset=utf-8")).
                and().
                header("Connection",equalTo("keep-alive")).
                and().
                body("id", equalTo(id)).
                and().
                body("userId", equalTo(userId)).
                and().
                body("title", equalTo(title)).
                and().
                body("body", equalTo(body));
    }

    @Test
    public void test_Delete_Post() {

        given().
                when().
                delete(URL + id).
                then().
                assertThat().
                statusCode(200).
                and().
                contentType(ContentType.JSON).
                and().
                header("Content-Type",equalTo("application/json; charset=utf-8")).
                and().
                header("Connection",equalTo("keep-alive")).
                and().
                body(equalTo("{}"));
    }


    @Test
    public void test_Create_Post() {

        String data = "{\"userId\": " + userId + ", \"title\": " + title + ", \"body\": " + body + "}";
        given().
                body(data).
                when().
                post(URL).
                then().
                assertThat().
                statusCode(201).
                and().
                contentType(ContentType.JSON).
                and().
                header("Content-Type",equalTo("application/json; charset=utf-8")).
                and().
                header("Connection",equalTo("keep-alive")).
                and().
                body("id", equalTo(101));

    }


    @Test
    public void test_Update_Post() {

        String data = "{\"id\": " + id + ", \"userId\": " + userId + ", \"title\": " + title + ", \"body\": " + body + "}";
        given().
                body(data).
                when().
                put(URL + id).
                then().
                assertThat().
                statusCode(200).
                and().
                contentType(ContentType.JSON).
                and().
                header("Content-Type",equalTo("application/json; charset=utf-8")).
                and().
                header("Connection",equalTo("keep-alive")).
                and().
                body("id", equalTo(id));

    }

    @Test
    public void test_List_Posts() {

        given().
                when().
                get(URL).
                then().
                assertThat().
                statusCode(200).
                and().
                contentType(ContentType.JSON).
                and().
                header("Content-Type",equalTo("application/json; charset=utf-8")).
                and().
                header("Connection",equalTo("keep-alive")).
                and().
                body("id", hasItem(id)).
                and().
                body("userId", hasItem(userId)).
                and().
                body("title", hasItem(title)).
                and().
                body("body", hasItem(body));
    }

}
