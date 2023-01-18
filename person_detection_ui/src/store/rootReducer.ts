import { combineReducers } from '@reduxjs/toolkit';
import imageApi from './image/api';

const rootReducer = combineReducers({
  [imageApi.reducerPath]: imageApi.reducer,
});

const rootMiddleware = [imageApi.middleware];

export { rootReducer, rootMiddleware };
