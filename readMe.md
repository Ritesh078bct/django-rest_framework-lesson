# Django REST Framework Learning Project

This project is a summary of my learning journey with Django's JSONResponse and Django REST Framework (DRF). I built several small applications like **Blogs**, **Students**, and **Employee Management** to practice and understand how to create powerful APIs using DRF.

---

## 🚀 What I Learned

### ✅ Using `JsonResponse` in Django

Before moving to Django REST Framework, I learned how to use Django's built-in `JsonResponse` to return JSON data from a view.

#### Pros of JsonResponse:
- Easy to use for simple APIs.
- No external library required.
- Useful for basic JSON responses.

#### Cons of JsonResponse:
- No built-in support for serialization.
- Difficult to manage large or complex data structures.
- No automatic validation of data.
- Lacks many features like pagination, filtering, etc.

This is where Django REST Framework becomes very useful.

---

## 🔧 Transition to Django REST Framework (DRF)

After understanding the limitations of `JsonResponse`, I moved to Django REST Framework to build full-featured APIs.

### 📱 Apps Created
- Blog App
- Student Management App
- Employee Management App

### 📦 Core Concepts Implemented

#### 1. **Serializers**
- Used to convert complex data types like Django models into JSON.
- Also used to validate incoming data.
- Learned about both simple and **nested serializers** (e.g., a blog post with its author data).

#### 2. **Views**
- Implemented both **Function-Based Views (FBVs)** and **Class-Based Views (CBVs)**.
- Learned how to use `@api_view` for FBVs.
- Used `APIView`, `GenericAPIView`, and **ViewSets** for CBVs.

#### 3. **Mixins and Generics**
- Used **Mixins** like `ListModelMixin`, `CreateModelMixin` for reusable code.
- Combined mixins with **GenericAPIView** to make the code clean and modular.
- Explored **Generic Views** like `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`.

#### 4. **Pagination**
- Implemented both **default pagination** and **custom pagination** to control how many results are shown per page.

#### 5. **Filtering, Searching, and Ordering**
- Used DRF’s built-in **filtering**, **search**, and **ordering** features.
- Also created **custom filters** to filter data based on specific needs.

---

## 🧠 Key Takeaways

- Django REST Framework makes building APIs **faster**, **cleaner**, and more **powerful** than using plain Django `JsonResponse`.
- Serializers are the **heart of DRF**, helping in both **data conversion** and **validation**.
- DRF gives a lot of built-in tools like pagination, filtering, and authentication, which makes development easier and more professional.
- By combining **views**, **mixins**, and **generics**, I learned to build reusable and scalable API code.

---

## 📂 Folder Structure (Example)

