import { configureStore } from '@reduxjs/toolkit';

import { rootMiddleware, rootReducer } from './rootReducer';

const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(rootMiddleware),
});

export type RootState = ReturnType<typeof rootReducer>;

export { store };
