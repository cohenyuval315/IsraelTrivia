// App.tsx
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import WelcomePage from './Screens/WelcomePage';
import LoginPage from './Screens/LoginPage';
import RegisterPage from './Screens/RegisterPage';

const Stack = createStackNavigator();

const App: React.FC = () => {
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen name="Welcome" component={WelcomePage}/>
                <Stack.Screen name="Login"   component={LoginPage}/>
                <Stack.Screen name="Register" component={RegisterPage}/>
            </Stack.Navigator>
        </NavigationContainer>
    );
};
export default App;
