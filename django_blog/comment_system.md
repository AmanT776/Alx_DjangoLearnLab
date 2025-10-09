# 📝 Django Blog Comment System Documentation

## Overview
The Comment System allows users to interact with blog posts by leaving their thoughts, feedback, or questions. It provides a controlled and secure environment where users can add, edit, and delete comments while maintaining proper visibility and permissions.

---

## Features
- Add Comments: Authenticated users can post comments directly under a blog post.
- Edit Comments: Users can edit their own comments if they need to make corrections or updates.
- Delete Comments: Users can delete their own comments with a confirmation prompt.
- Comment Visibility: Only published comments are visible to all visitors.
- Permission Management: Only the author of a comment can edit or delete it, while admins can moderate all comments if needed.

---

## Workflow

### 1. Adding a Comment
1. A logged-in user navigates to a blog post.
2. The user sees a comment form under the post.
3. The user types a comment and submits it.
4. The system validates the comment (e.g., ensuring it's not empty or too short).
5. Once validated, the comment is saved and displayed immediately under the post.

#### Rules & Permissions
- Only authenticated users can post comments.
- The comment must meet minimum content requirements (e.g., length).
- The comment is linked to the user who posted it and the specific blog post.

---

### 2. Editing a Comment
1. The comment author sees an **Edit** option next to their own comment.
2. Clicking **Edit** opens a form with the comment’s current content.
3. The user can update the comment and submit it.
4. After submission, the comment is updated and the changes are displayed under the post.

#### Rules & Permissions
- Only the original author of a comment can edit it.
- Other users cannot see an edit option on comments they did not create.
- Edits are timestamped to track when a comment was modified.

---

### 3. Deleting a Comment
1. The comment author sees a **Delete** option next to their own comment.
2. Clicking **Delete** opens a confirmation prompt.
3. The user confirms the deletion.
4. The comment is permanently removed from the post.

#### Rules & Permission
- Only the original author can delete their comment.
- A confirmation step prevents accidental deletion.
- Once deleted, the comment cannot be restored unless there is an admin intervention.

---

### 4. Comment Visibility
- All comments linked to a published post are visible to any visitor.
- Unauthenticated users can view comments but cannot add, edit, or delete them.
- Only the author and admins (if moderation is implemented) have the ability to modify or remove comments.
- Deleted comments are immediately removed from the post view.



### 6. User Interaction Flow

1. Visitor**: Can view posts and all associated comments.
2. Logged-in User: Can view, add, edit, and delete their own comments.
3. Admin: Can manage all comments, including editing or deleting inappropriate content.
