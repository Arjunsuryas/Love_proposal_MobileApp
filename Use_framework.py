import { useEffect } from 'react';

// Extend the Window interface globally to include our custom function
declare global {
  interface Window {
    frameworkReady?: () => void;
  }
}

// Custom hook
export function useFrameworkReady() {
  useEffect(() => {
    // Call the global frameworkReady function if it exists
    window.frameworkReady?.();
  }, []); // Empty dependency array ensures it runs once on mount
}
