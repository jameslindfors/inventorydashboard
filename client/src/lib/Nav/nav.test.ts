import { render, screen, fireEvent } from '@testing-library/svelte';
import Nav from './Nav.svelte';

describe('Nav', () => {
	test("that the heading is 'Inventory Manager'", () => {
		render(Nav);
		const title = screen.getAllByRole('heading');
		expect(title[0]).toHaveTextContent('Inventory Manager');
	});
});
