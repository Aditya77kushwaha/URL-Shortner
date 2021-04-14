A URL shortner takes a URL and returns a shorter version of the same.
The idea is to assign to each URL entered a unique ID and store the URL and the corresponding ID in the database.
The ID is then appended to the app's URL, this is the required shorter URL.
The concept of dynamic URLs of Django comes into play now.
Django fetches the ID appended at the last of the shortened URL and redirects to the corresponding URL stored in database.
