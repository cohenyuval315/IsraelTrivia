import React, { useEffect, useState } from 'react';

const useFontLoader = (fontLoader) => {
    const [fontLoaded, setFontLoaded] = useState(false);

    useEffect(() => {
        const loadFonts = async () => {
            try {
                await fontLoader();
                setFontLoaded(true);
            } catch (error) {
                console.error('Error loading fonts:', error);
                // Optionally, you can handle the error in a way that makes sense for your application
            }
        };

        loadFonts();
    }, [fontLoader]);

    return fontLoaded;
};

export default useFontLoader;
