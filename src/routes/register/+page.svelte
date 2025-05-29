<script lang="ts">
	import { toast } from 'svelte-sonner';
	import { onMount, getContext, tick } from 'svelte';
	import { goto } from '$app/navigation';
	import { getBackendConfig } from '$lib/apis';
	import { userSignUp } from '$lib/apis/auths';
	import { WEBUI_NAME, config, user, socket } from '$lib/stores';
	import { generateInitialsImage } from '$lib/utils';
	import Spinner from '$lib/components/common/Spinner.svelte';
	import { WEBUI_BASE_URL } from '$lib/constants';

	const i18n = getContext('i18n');

	let loaded = false;
	let name = '';
	let email = '';
	let password = '';
	let confirmPassword = '';

	const querystringValue = (key: string): string | null => {
		const querystring = window.location.search;
		const urlParams = new URLSearchParams(querystring);
		return urlParams.get(key);
	};

	const setSessionUser = async (sessionUser: any) => {
		if (sessionUser) {
			toast.success($i18n.t(`You're now registered and logged in.`));
			if (sessionUser.token) {
				localStorage.token = sessionUser.token;
			}
			$socket?.emit('user-join', { auth: { token: sessionUser.token } });
			await user.set(sessionUser);
			await config.set(await getBackendConfig());

			const redirectPath = querystringValue('redirect') || '/';
			goto(redirectPath);
		}
	};

	const signUpHandler = async () => {
		if (password !== confirmPassword) {
			toast.error($i18n.t('Passwords do not match'));
			return;
		}

		const sessionUser = await userSignUp(name, email, password, generateInitialsImage(name)).catch(
			(error) => {
				toast.error(`${error}`);
				return null;
			}
		);

		await setSessionUser(sessionUser);
	};

	async function setLogoImage() {
		await tick();
		const logo = document.getElementById('logo') as HTMLImageElement;

		if (logo) {
			const isDarkMode = document.documentElement.classList.contains('dark');

			if (isDarkMode) {
				const darkImage = new Image();
				darkImage.src = '/static/favicon-dark.png';

				darkImage.onload = () => {
					logo.src = '/static/favicon-dark.png';
					logo.style.filter = '';
				};

				darkImage.onerror = () => {
					logo.style.filter = 'invert(1)';
				};
			}
		}
	}

	onMount(async () => {
		loaded = true;
		setLogoImage();
		// Force light mode
		document.documentElement.classList.remove('dark');
		document.documentElement.classList.add('light');
	});
</script>

<svelte:head>
	<title>
		{`Register - ${$WEBUI_NAME}`}
	</title>
</svelte:head>

<div class="light w-full h-screen max-h-[100dvh] bg-white text-gray-900 relative">
	<div class="w-full h-full absolute top-0 left-0 bg-white"></div>
	<div class="w-full absolute top-0 left-0 right-0 h-8 drag-region" />

	{#if loaded}
		<div class="fixed m-10 z-50">
			<div class="flex space-x-2">
				<div class="self-center">
					<img
						id="logo"
						crossorigin="anonymous"
						src="{WEBUI_BASE_URL}/static/splash.png"
						class="w-6 rounded-full"
						alt=""
					/>
				</div>
			</div>
		</div>

		<div class="fixed min-h-screen w-full flex font-primary z-50">
			<!-- Left side - Register -->
			<div class="w-full md:w-1/2 px-6 md:px-10 min-h-screen flex flex-col bg-white text-gray-900">
				<div class="my-auto pb-10 w-full max-w-md mx-auto">
					<div class="text-gray-900">
						<form
							class="flex flex-col justify-center"
							on:submit={(e) => {
								e.preventDefault();
								signUpHandler();
							}}
						>
							<div class="mb-1">
								<div class="text-2xl font-medium">
									{$i18n.t(`Create your {{WEBUI_NAME}} account`, { WEBUI_NAME: $WEBUI_NAME })}
								</div>
							</div>

							<div class="flex flex-col mt-4">
								<div class="mb-2">
									<label for="name" class="text-sm font-medium text-left mb-1 block"
										>{$i18n.t('Name')}</label
									>
									<input
										bind:value={name}
										type="text"
										id="name"
										class="my-0.5 w-full text-sm outline-none bg-transparent border border-gray-200 rounded-lg px-3 py-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all"
										autocomplete="name"
										placeholder={$i18n.t('Enter Your Full Name')}
										required
									/>
								</div>

								<div class="mb-2">
									<label for="email" class="text-sm font-medium text-left mb-1 block"
										>{$i18n.t('Email')}</label
									>
									<input
										bind:value={email}
										type="email"
										id="email"
										class="my-0.5 w-full text-sm outline-none bg-transparent border border-gray-200 rounded-lg px-3 py-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all"
										autocomplete="email"
										name="email"
										placeholder={$i18n.t('Enter Your Email')}
										required
									/>
								</div>

								<div class="mb-2">
									<label for="password" class="text-sm font-medium text-left mb-1 block"
										>{$i18n.t('Password')}</label
									>
									<input
										bind:value={password}
										type="password"
										id="password"
										class="my-0.5 w-full text-sm outline-none bg-transparent border border-gray-200 rounded-lg px-3 py-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all"
										placeholder={$i18n.t('Enter Your Password')}
										autocomplete="new-password"
										name="new-password"
										required
									/>
								</div>

								<div>
									<label for="confirm-password" class="text-sm font-medium text-left mb-1 block"
										>{$i18n.t('Confirm Password')}</label
									>
									<input
										bind:value={confirmPassword}
										type="password"
										id="confirm-password"
										class="my-0.5 w-full text-sm outline-none bg-transparent border border-gray-200 rounded-lg px-3 py-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all"
										placeholder={$i18n.t('Confirm Your Password')}
										autocomplete="new-password"
										required
									/>
								</div>
							</div>

							<div class="mt-5">
								<button
									class="bg-gray-700/5 hover:bg-gray-700/10 dark:bg-gray-100/5 dark:hover:bg-gray-100/10 dark:text-gray-300 dark:hover:text-white transition w-full rounded-full font-medium text-sm py-2.5"
									type="submit"
								>
									{$i18n.t('Create Account')}
								</button>

								<div class="mt-4 text-sm text-center">
									{$i18n.t('Already have an account?')}
									<a href="/auth" class="font-medium underline">
										{$i18n.t('Sign in')}
									</a>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>

			<!-- Right side - OmicsAgent Description -->
			<div
				class="hidden md:flex w-1/2 min-h-screen flex-col bg-gradient-to-br from-blue-50 to-white"
			>
				<div class="my-auto px-10 max-w-xl mx-auto">
					<h1
						class="text-4xl font-bold mb-6 bg-gradient-to-r from-blue-700 to-purple-700 bg-clip-text text-transparent"
					>
						Welcome to OmicsAgent
					</h1>
					<p class="text-lg mb-8 text-gray-700">All The Bioinformatics Tools. One Brain.</p>
					<div class="space-y-8">
						<div class="flex items-start space-x-4">
							<div class="flex-shrink-0 mt-1">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									class="h-6 w-6 text-blue-600"
									fill="none"
									viewBox="0 0 24 24"
									stroke="currentColor"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
									/>
								</svg>
							</div>
							<div>
								<h3 class="font-semibold mb-2 text-gray-900">Automated Analysis</h3>
								<p class="text-gray-700">
									We handle the algorithms — you focus on the discoveries.
								</p>
							</div>
						</div>
						<div class="flex items-start space-x-4">
							<div class="flex-shrink-0 mt-1">
								<svg
									xmlns="http://www.w3.org/2000/svg"
									class="h-6 w-6 text-blue-600"
									fill="none"
									viewBox="0 0 24 24"
									stroke="currentColor"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M13 10V3L4 14h7v7l9-11h-7z"
									/>
								</svg>
							</div>
							<div>
								<h3 class="font-semibold mb-2 text-gray-900">Powerful Integration</h3>
								<p class="text-gray-700">
									Bring together multi-omics data, workflows, and insights into a single intelligent
									workspace.
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	{/if}
</div>
