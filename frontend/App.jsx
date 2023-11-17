// App.jsx
import React, { useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import WelcomeScreen from './screens/WelcomeScreen/WelcomeScreen';
import LoginScreen from './screens/LoginScreen/LoginScreen';
import RegisterScreen from './screens/RegisterScreen/RegisterScreen';
import MainScreen from './screens/MainScreen/MainScreen';
import TriviaScreen from "./screens/TriviaScreen";


const Stack = createStackNavigator();
//const Tab = createBottomTabNavigator();

const Stack1 = () => {
    return (
        <Stack.Navigator initialRouteName="Welcome" >
            <Stack.Screen name="Welcome"    component={WelcomeScreen}  />
            <Stack.Screen name="Login"      component={LoginScreen} />
            <Stack.Screen name="Register"   component={RegisterScreen} />
        </Stack.Navigator>
    );
};

const Stack2 = () => {
    return (
        <Stack.Navigator initialRouteName="Main">
            <Stack.Screen name="Main" component={MainScreen} />
            <Stack.Screen name="Trivia" component={TriviaScreen} />
        </Stack.Navigator>
    );
};

const App = () => {

    const isLogin = true
    return (
        <NavigationContainer>
            <Stack.Navigator screenOptions={{ headerShown: false }}>
                {isLogin &&  <Stack.Screen name="Stack1" component={Stack1} />}
                {isLogin &&  <Stack.Screen name="Stack2" component={Stack2} />}
            </Stack.Navigator>
        </NavigationContainer>
    );
};

export default App;
