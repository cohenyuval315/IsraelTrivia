// LinearGradientBackground.jsx
import React from 'react';
import { LinearGradient } from 'expo-linear-gradient';

const LinearGradientBackground = ({ children }) => {
    return (
        <LinearGradient
            colors={['#6DE5B5', '#0039C0']}
            start={{ x: 1.2, y: 0 }}
            end={{ x: 0, y: 1 }}
            style={{ flex: 1 }}
        >
            {children}
        </LinearGradient>
    );
};

export default LinearGradientBackground;
