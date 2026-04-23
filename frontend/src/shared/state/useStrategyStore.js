import { create } from "zustand";

export const useStrategyStore = create((set) => ({
  strategies: [],
  selectedStrategy: null,

  setStrategies: (strategies) => set({ strategies }),
  selectStrategy: (strategy) => set({ selectedStrategy: strategy }),
  addStrategy: (strategy) =>
    set((state) => ({ strategies: [...state.strategies, strategy] })),
  removeStrategy: (strategyId) =>
    set((state) => ({
      strategies: state.strategies.filter((strategy) => strategy.id !== strategyId),
      selectedStrategy:
        state.selectedStrategy?.id === strategyId ? null : state.selectedStrategy,
    })),
}));
