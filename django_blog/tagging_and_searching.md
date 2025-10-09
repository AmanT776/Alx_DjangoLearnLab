
---

## Search Functionality

### Purpose
Allows users to **search posts** using keywords in:
- Post titles
- Post content
- Post tags

### Features
- Search bar is available on the posts list page.
- Supports partial matches and multiple parameters using Django’s `Q` objects.
- Search results update dynamically when a query is entered.
- The search form preserves the query after submission for user convenience.

### How Search Works
1. User enters a search term in the search bar.
2. The backend filters posts with the following logic:
 - `title__icontains=query` → matches post titles containing the query.
 - `content__icontains=query` → matches post content containing the query.
 - `tags__name__icontains=query` → matches posts with tags containing the query.
3. Duplicate results are removed using `.distinct()`.
4. The filtered list is displayed on the posts list page, showing matching posts.

## User Permissions

- **Tagging**
- Only **authors** can add or edit tags while creating/updating posts.
- Tags are public and visible to all users.
- **Search**
- Available to **all users**, including non-authenticated visitors.

---

## Best Practices

- Use meaningful, concise tags to improve content discovery.
- Avoid creating duplicate or unnecessary tags.
- Keep search queries simple for better performance.
- Ensure the search form is visible and easy to use on the posts page.

---

## Future Enhancements

- Make tags clickable to filter posts by a specific tag.
- Add autocomplete suggestions in the search bar based on existing tags.
- Allow users to subscribe to tags for notifications when new posts are added.
