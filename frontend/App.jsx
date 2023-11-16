// App.jsx
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import WelcomeScreen from './screens/WelcomeScreen';
import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';
import MainScreen from './screens/MainScreen';

const Stack = createStackNavigator();
//const Tab = createBottomTabNavigator();

const Stack1 = () => {
    return (
        <Stack.Navigator initialRouteName="Welcome" >
            <Stack.Screen name="Welcome"    component={WelcomeScreen} />
            <Stack.Screen name="Login"      component={LoginScreen} />
            <Stack.Screen name="Register"   component={RegisterScreen} />
        </Stack.Navigator>
    );
};

const Stack2 = () => {
    return (
        <Stack.Navigator initialRouteName="Main">
            <Stack.Screen name="Main" component={MainScreen} />
        </Stack.Navigator>
    );
};

const App = () => {
    return (
        <NavigationContainer>
            <Stack.Navigator screenOptions={{ headerShown: false }}>
                <Stack.Screen name="Stack1" component={Stack1} />
                <Stack.Screen name="Stack2" component={Stack2} />
            </Stack.Navigator>
        </NavigationContainer>
    );
};

export default App;
