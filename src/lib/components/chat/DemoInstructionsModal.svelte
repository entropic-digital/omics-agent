<script lang="ts">
	import { getContext, onMount } from 'svelte';
	import Modal from '../common/Modal.svelte';

	const i18n = getContext('i18n');

	export let show = false;

	const STORAGE_KEY = 'demo-instructions-hidden';

	onMount(() => {
		// Check if user has previously chosen to hide the modal
		const hidden = localStorage.getItem(STORAGE_KEY);
		if (hidden === 'true') {
			show = false;
		}
	});

	function hideForever() {
		localStorage.setItem(STORAGE_KEY, 'true');
		show = false;
	}
</script>

<Modal bind:show size="sm">
	<div>
		<div class="flex justify-between dark:text-gray-100 px-5 pt-4 pb-2">
			<div class="text-lg font-medium self-center font-primary">
				{$i18n.t('Demo Instructions')}
			</div>
			<button
				class="self-center"
				on:click={() => {
					show = false;
				}}
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 20 20"
					fill="currentColor"
					class="w-5 h-5"
				>
					<path
						d="M6.28 5.22a.75.75 0 00-1.06 1.06L8.94 10l-3.72 3.72a.75.75 0 101.06 1.06L10 11.06l3.72 3.72a.75.75 0 101.06-1.06L11.06 10l3.72-3.72a.75.75 0 00-1.06-1.06L10 8.94 6.28 5.22z"
					/>
				</svg>
			</button>
		</div>

		<div class="px-5 pb-4 text-gray-600 dark:text-gray-300">
			<ol class="list-decimal list-inside space-y-2">
				<li>
					Download data from:
					<a
						href="https://download-directory.github.io?url=https://github.com/dionizijefa/iscb-bioinformatics-agents/tree/master/data"
						class="text-blue-600 dark:text-blue-400 hover:underline break-all"
						target="_blank"
						rel="noopener noreferrer"
					>
						download-directory.github.io
					</a>
				</li>
				<li>Upload the data using the "+" button</li>
				<li>
					Use the following prompt:<br />
					<span class="text-gray-700 font-bold dark:text-gray-300 pl-4 block mt-1">
						"Run transcript quantification pipeline"
					</span>
					<span class="text-sm text-gray-500 dark:text-gray-400"
						>(You don't have to remember it, it is suggested by default)</span
					>
				</li>
			</ol>
			<div class="mt-6 flex justify-end">
				<button
					class="px-4 py-2 text-sm rounded-lg bg-gray-100 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-700 dark:text-gray-200 transition-colors duration-200"
					on:click={hideForever}
				>
					Don't show this again
				</button>
			</div>
		</div>
	</div>
</Modal>
