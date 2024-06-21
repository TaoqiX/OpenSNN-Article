# Vite中环境变量管理
> 在Vue 3 项目中使用 Vite 进行构建时，环境变量的管理和使用与 Vue CLI 略有不同。以下是如何在 Vite 项目中使用环境变量的详细步骤。


### 1. 创建环境变量文件

在项目根目录下创建不同的 `.env` 文件，这些文件可以根据不同的环境来配置。

- `.env`：适用于所有环境的默认配置。
- `.env.development`：仅适用于开发环境。
- `.env.production`：仅适用于生产环境。

#### 例如：

**.env**

```plaintext
VITE_APP_TITLE=My Vite App
```

**.env.development**

```plaintext
VITE_APP_API_URL=http://localhost:3000
VITE_APP_DEBUG=true
```

**.env.production**

```plaintext
VITE_APP_API_URL=https://api.example.com
VITE_APP_DEBUG=false
```

### 2. 访问环境变量

在 Vite 项目中，环境变量可以通过 `import.meta.env` 来访问。注意：所有自定义环境变量都应该以 `VITE_` 前缀开头。

例如，在组件或 JavaScript 文件中：

```javascript
console.log(import.meta.env.VITE_APP_API_URL);
console.log(import.meta.env.VITE_APP_TITLE);
console.log(import.meta);    // 直接打印 import.meta 看一看
```

### 3. 在组件中使用环境变量

你可以在 Vue 组件中使用环境变量，通过 `setup` 函数或 `computed` 属性来访问这些变量。

#### 在 `setup` 函数中使用：

```vue
<template>
  <div>
    <p>API URL: {{ apiUrl }}</p>
    <p>App Title: {{ title }}</p>
  </div>
</template>

<script>
export default {
  setup() {
    const apiUrl = import.meta.env.VITE_APP_API_URL;
    const title = import.meta.env.VITE_APP_TITLE;

    return { apiUrl, title };
  }
}
</script>
```

#### 在 `computed` 属性中使用：

```vue
<template>
  <div>
    <p>API URL: {{ apiUrl }}</p>
    <p>App Title: {{ title }}</p>
  </div>
</template>

<script>
export default {
  computed: {
    apiUrl() {
      return import.meta.env.VITE_APP_API_URL;
    },
    title() {
      return import.meta.env.VITE_APP_TITLE;
    }
  }
}
</script>
```

### 4. 使用不同的环境模式

1. **development**：`vite` 或 `vite serve` 使用。
2. **production**：`vite build` 使用。

你也可以自定义其他模式，例如：

```bash
vite build --mode staging
```

然后创建对应的 `.env.staging` 文件。

### 5. 动态使用环境变量

如果你需要在模板中使用环境变量，可以将它们绑定到组件的 `setup` 或 `data` 中：

```vue
<template>
  <div>
    <p>API URL: {{ apiUrl }}</p>
    <p>App Title: {{ title }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      apiUrl: import.meta.env.VITE_APP_API_URL,
      title: import.meta.env.VITE_APP_TITLE
    }
  }
}
</script>
```

### 总结

在使用 Vite 的 Vue 3 项目中，环境变量管理通过 `.env` 文件和 `import.meta.env` 进行。确保自定义的环境变量以 `VITE_` 前缀开头，以便能够在代码中正确访问这些变量。这种方式提供了一个灵活和简洁的方法来管理不同环境下的配置。

> 官方介绍：[https://cn.vitejs.dev/guide/env-and-mode.html](https://cn.vitejs.dev/guide/env-and-mode.html)



######

-----

【转载自:】**开思通智网** ---- “一起来o站，玩转AGI！”  
【官网:】[https://www.opensnn.com/](https://www.opensnn.com/)  
【原文链接:】[https://www.opensnn.com/os/article/10000837](https://www.opensnn.com/os/article/10000837)

##### 结束
