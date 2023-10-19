package platform.work6.core;

import platform.work6.annotations.*;

import java.io.File;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.net.URL;
import java.util.*;

public class MyApplicationContext {
    private Map<Class<?>, Object> beanRegistry = new HashMap<>();
    private List<Object> beansToAutowire = new ArrayList<>();
    private Map<Object, Method> postConstructMethodRegistry = new HashMap<>();
    private Map<Object, Method> preDestroyMethodRegistry = new HashMap<>();
    public MyApplicationContext(String basePackage) {
        scanAndRegisterBeans(basePackage);
        processAutowiring();
        initializeBeans();
    }

    private void scanAndRegisterBeans(String basePackage) {
        basePackage = basePackage.replace('.', '/');
        ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
        URL resource = classLoader.getResource(basePackage);
        File directory = new File(Objects.requireNonNull(resource).getFile());

        for (File file : Objects.requireNonNull(directory.listFiles())) {
            if (file.isDirectory()) {
                scanAndRegisterBeans(basePackage + '/' + file.getName());
            } else if (file.getName().endsWith(".class")) {
                String className = file.getName().substring(0, file.getName().length() - 6);
                try {
                    Class<?> clazz = Class.forName(basePackage.replace('/', '.') + '.' + className);
                    if (clazz.isAnnotationPresent(MyRepository.class)
                            || clazz.isAnnotationPresent(MyService.class)
                            || clazz.isAnnotationPresent(MyRestController.class)) {
                        registerBean(clazz);
                    }
                } catch (ClassNotFoundException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    private void processAutowiring() {
        for (Object bean : beansToAutowire) {
            for (Field field : bean.getClass().getDeclaredFields()) {
                if (field.isAnnotationPresent(MyAutowired.class)) {
                    Object dependency = beanRegistry.get(field.getType());
                    if (dependency != null) {
                        field.setAccessible(true);
                        try {
                            field.set(bean, dependency);
                        } catch (IllegalAccessException e) {
                            e.printStackTrace();
                        }
                    }
                }
            }
        }
    }

    public <T> void registerBean(Class<? extends T> beanClass) {
        try {
            Constructor<? extends T> constructor = beanClass.getDeclaredConstructor();
            T instance = constructor.newInstance();
            for (Method method : beanClass.getDeclaredMethods()) {
                if (method.isAnnotationPresent(PostConstruct.class)) {
                    postConstructMethodRegistry.put(instance, method);
                } else if (method.isAnnotationPresent(PreDestroy.class)) {
                    preDestroyMethodRegistry.put(instance, method);
                }
            }
            beanRegistry.put(beanClass, instance);
            beansToAutowire.add(instance);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public <T> T getBean(Class<T> type) {
        return type.cast(beanRegistry.get(type));
    }

    public void close() {
        for (Map.Entry<Object, Method> entry : preDestroyMethodRegistry.entrySet()) {
            try {
                Method method = entry.getValue();
                method.setAccessible(true);
                method.invoke(entry.getKey());
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    private void initializeBeans() {
        for (Map.Entry<Object, Method> entry : postConstructMethodRegistry.entrySet()) {
            try {
                Method method = entry.getValue();
                method.setAccessible(true);
                method.invoke(entry.getKey());
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }


}
